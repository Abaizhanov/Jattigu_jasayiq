import React, { useEffect, useState, useContext } from 'react';
import BlogItems from '../components/BlogItems';
import AuthContext from '../context/AuthContext'; // Import your AuthContext

export default function BlogPage() {
  const { authTokens } = useContext(AuthContext); // Get the authTokens from context
  const [posts, setPosts] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    if (authTokens) {
      // Fetch blog posts with authorization token
      fetch('http://127.0.0.1:8000/blogs/posts/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authTokens.access}`, // Attach token
        },
      })
        .then((response) => response.json())
        .then((data) => setPosts(data))
        .catch((error) => console.error('Error fetching posts:', error));

      // Fetch categories with authorization token
      fetch('http://127.0.0.1:8000/blogs/categories', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authTokens.access}`, // Attach token
        },
      })
        .then((response) => response.json())
        .then((data) => setCategories(data))
        .catch((error) => console.error('Error fetching categories:', error));
    }
  }, [authTokens]);

  return (
    <div className="ml-36">
      <p className="mb-2">Blog</p>
      <h1 className="text-3xl font-bold mb-2">Healthy Body & Mind</h1>
      <p className="text-xl">
        Research-backed fitness articles to help you care for your <br /> body
        and mind.
      </p>

      {/* Categories */}
      <div className="mt-5">
        <h2 className="text-xl font-semibold mb-4">Categories</h2>
        <div className="flex flex-wrap gap-4">
          {categories.map((category) => (
            <span
              key={category.id}
              className="bg-gray-200 px-4 py-2 rounded-full text-sm"
            >
              {category.name}
            </span>
          ))}
        </div>
      </div>

      {/* Blog Posts */}
      <div className="mt-10">
        {posts.map((post) => (
          <BlogItems
            key={post.id}
            post={post}
          />
        ))}
      </div>
    </div>
  );
}
