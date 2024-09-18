from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    bag = request.session.get('bag', {})

    # Check if the item already exists in the bag
    if item_id in bag:
        # If size is specified
        if size:
            # Check if the item has a size and if it exists in 'items_by_size'
            if 'items_by_size' in bag[item_id]:
                if size in bag[item_id]['items_by_size']:
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = quantity
            else:
                # Initialize 'items_by_size' for this item
                bag[item_id]['items_by_size'] = {size: quantity}
        else:
            # If no size, simply add to the quantity
            if 'items_by_size' in bag[item_id]:
                # Handle items without size uniformly, add a None key
                if None in bag[item_id]['items_by_size']:
                    bag[item_id]['items_by_size'][None] += quantity
                else:
                    bag[item_id]['items_by_size'][None] = quantity
            else:
                # Initialize 'items_by_size' for no-size products
                bag[item_id]['items_by_size'] = {None: quantity}
    else:
        # If the item does not exist in the bag, add it
        if size:
            bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            bag[item_id] = {'items_by_size': {None: quantity}}

    # Update the session with the new bag data
    request.session['bag'] = bag
    return redirect(redirect_url)
