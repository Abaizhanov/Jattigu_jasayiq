import React from 'react';
import { Link } from 'react-router-dom';

const BlogItems = ({ post }) => {
  const { title, content, image, time_to_read, categories } = post;

  return (
    <div className="bg-white rounded-lg shadow-lg mb-6 p-6">
      {/* Blog Image */}
      <img
        src={image}
        alt={title}
        className="w-full h-64 object-cover rounded-lg mb-6"
      />

      {/* Title and Content */}
      <h2 className="text-2xl font-semibold mb-4">{title}</h2>
      <p className="text-gray-700 mb-4">{content.slice(0, 150)}...</p>

      {/* Time to Read */}
      <p className="text-gray-500 mb-4">
        Time to read: {time_to_read} minute(s)
      </p>

      {/* Categories */}
      <div className="mb-4">
        <h3 className="text-lg font-semibold mb-2">Categories:</h3>
        <div className="flex gap-2">
          {categories.map((category) => (
            <Link
              key={category.id}
              to={`/blog/category/${category.slug}`}
              className="bg-gray-200 px-4 py-2 rounded-full text-sm"
            >
              {category.name}
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default BlogItems;
