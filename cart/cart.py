class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            pass
        else:
            self.cart[item_id] = {'price': str(item.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
