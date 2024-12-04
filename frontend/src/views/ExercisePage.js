import React, { useState, useEffect, useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext'; // Import your AuthContext

const ExercisePage = () => {
  const { authTokens } = useContext(AuthContext); // Access authTokens from context
  const [categories, setCategories] = useState([]);
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    if (authTokens) {
      // Fetch categories with the token in the header
      fetch('http://127.0.0.1:8000/exercises/exercise_categories/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authTokens.access}`, // Attach token
        },
      })
        .then((res) => res.json())
        .then((data) => setCategories(data));

      // Fetch exercises with the token in the header
      fetch('http://127.0.0.1:8000/exercises/exercises/', {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authTokens.access}`, // Attach token
        },
      })
        .then((res) => res.json())
        .then((data) => setExercises(data));
    }
  }, [authTokens]);

  const getExercisesByCategory = (categoryId) => {
    return exercises.filter((exercise) =>
      exercise.category.some((cat) => cat.id === categoryId)
    );
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">
        Exercise Categories
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {categories.map((category) => (
          <div
            key={category.id}
            className="bg-white rounded-lg shadow-lg p-4 text-center"
          >
            <img
              src={category.image}
              alt={category.name}
              className="w-24 mx-auto rounded-full object-cover mb-4"
            />
            <h2 className="text-xl font-semibold mb-4">{category.name}</h2>
            <ul className="text-gray-700 text-sm space-y-2">
              {getExercisesByCategory(category.id).map((exercise) => (
                <li
                  key={exercise.id}
                  className="hover:text-blue-500 cursor-pointer"
                >
                  <Link to={`/exercises/${exercise.id}`}>{exercise.name}</Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ExercisePage;
