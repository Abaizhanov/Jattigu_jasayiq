'use client';
import React from 'react';

const figures = [
  {
    count: '500+',
    label: 'Happy Members',
    description: 'Our community is growing fast',
  },
  {
    count: '500+',
    label: 'Happy Members',
    description: 'Our community is growing fast',
  },
  {
    count: '500+',
    label: 'Happy Members',
    description: 'Our community is growing fast',
  },
  {
    count: '500+',
    label: 'Happy Members',
    description: 'Our community is growing fast',
  },
];

export default function Figure() {
  return (
    <div className="bg-gray-900 h-[200px] text-white flex items-center">
      <div className="flex justify-between items-center w-full px-8">
        {figures.map((figure, index) => (
          <div
            key={index}
            className="flex-1 text-center"
          >
            <h2 className="text-[36px] font-bold">{figure.count}</h2>
            <p className="text-[14px] font-semibold">{figure.label}</p>
            <p className="text-[14px] font-semibold">{figure.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
