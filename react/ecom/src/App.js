import React, { useState } from 'react';

function App() {
  const [cartItems, setCartItems] = useState([]);
  const products = [
    {
      id: 1,
      name: 'Product 1',
      price: 10.99,
      image: 'https://p0.pxfuel.com/preview/50/864/1001/onion-white-isolated-whole.jpg',
    },
    {
      id: 2,
      name: 'Product 2',
      price: 19.99,
      image: 'https://p0.pxfuel.com/preview/889/458/354/chili-hot-ingredient-red.jpg',
    },
    {
      id: 3,
      name: 'Product 3',
      price: 7.99,
      image: 'https://p1.pxfuel.com/preview/793/451/730/yam-ipomoea-batatas-sweet-potato-white-potato-tuber-winds.jpg',
    },
  ];

  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };

  return (
    <div>
      <h1>My eCommerce Page</h1>
      <div>
        <div>
          <h2>Products</h2>
          {products.map((product) => (
            <div key={product.id}>
              <img src={product.image} alt={product.name} />
              <h3>{product.name}</h3>
              <p>{product.price}</p>
              <button onClick={() => addToCart(product)}>Add to cart</button>
            </div>
          ))}
        </div>

        <div>
          <h2>Shopping Cart</h2>
          {cartItems.map((item) => (
            <div key={item.id}>
              <h3>{item.name}</h3>
              <p>{item.price}</p>
            </div>
          ))}
          <div>
            <button>Checkout</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
