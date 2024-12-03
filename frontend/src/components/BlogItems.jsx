import React, { useEffect, useState } from 'react';

export default function BlogItems({ blog }) {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch('http://127.0.0.1:8000/blogs/posts/');
      const data = res.json();
      console.log(data);
    }

    fetchData();
  }, []);

  return (
    <div>
      <h2>{posts.names}</h2>
    </div>
  );
}
