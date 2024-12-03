import React from 'react';
import BlogItems from '../components/BlogItems';

const blog = [
  {
    id: 1,
    name: 'Muscle Building Fundamentals',
    slug: 'muscle-building-fundamentals',
  },
  {
    id: 2,
    name: 'Nutrition & Supplements',
    slug: 'nutrition-supplements',
  },
  {
    id: 3,
    name: 'Lifestyle',
    slug: 'lifestyle',
  },
];

export default function BlogPage() {
  return (
    <div className=" ml-36">
      <p className="mb-2">Blog</p>
      <h1 className="text-3xl font-bold mb-2">Healthy Body & Mind</h1>
      <p className="text-xl">
        Research-backed fitness articles to help you care for your <br /> body
        and mind.
      </p>
      <div className="mt-10">
        {blog.map((blog, i) => {
          return <BlogItems blog={blog} />;
        })}
      </div>
    </div>
  );
}
