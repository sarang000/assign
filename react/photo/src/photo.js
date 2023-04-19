import React from 'react';

function Photography() {
  const photos = [
    {
      id: 1,
      title: 'Photo 1',
      description: 'Blue Flag Golden Beach in Puri, Odisha',
      image: 'https://www.fabhotels.com/blog/wp-content/uploads/2022/01/Puri-1200x900-1.jpeg',
    },
    {
      id: 2,
      title: 'Photo 2',
      description: 'Butterfly Beach in South Goa',
      image: 'https://www.fabhotels.com/blog/wp-content/uploads/2019/02/Butterfly-Beach.jpg',
    },
    {
      id: 3,
      title: 'Photo 3',
      description: ' Om Beach in Gokarna, Karnataka',
      image: 'https://www.fabhotels.com/blog/wp-content/uploads/2022/01/7-Om-Beach_1936292293-.jpg',
    },
  ];

  return (
    <div>
      <header>
        <h1>My Photography Page</h1>
      </header>
      <main>
        <h2>My Photos</h2>
        <div className="photo-grid">
          {photos.map((photo) => (
            <div key={photo.id} className="photo-card">
              <img src={photo.image} alt={photo.title} />
              <h3>{photo.title}</h3>
              <p>{photo.description}</p>
            </div>
          ))}
        </div>
      </main>
      <footer>
        <p>© 2023 My Photography Page</p>
      </footer>
    </div>
  );
}

export default Photography;
