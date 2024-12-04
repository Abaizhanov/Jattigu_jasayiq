import React, { useState, useEffect, useContext } from 'react';
import { useParams } from 'react-router-dom';
import AuthContext from '../context/AuthContext'; // Import your AuthContext

const ExerciseItem = () => {
  const { authTokens } = useContext(AuthContext); // Access authTokens from context
  const { id } = useParams(); // Get the exercise id from the URL
  const [exercise, setExercise] = useState(null);
  const [equipment, setEquipment] = useState([]);
  const [muscles, setMuscles] = useState([]);

  useEffect(() => {
    if (authTokens) {
      // Fetch exercise details with the token in the header
      fetch(`http://127.0.0.1:8000/exercises/exercises/${id}/`, {
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authTokens.access}`, // Attach token
        },
      })
        .then((res) => res.json())
        .then((data) => {
          setExercise(data);
          console.log(data);
          // Fetch equipment categories associated with this exercise
          if (data.equipment_needed) {
            setEquipment(data.equipment_needed);
          }

          // Fetch muscles associated with this exercise
          if (data.category) {
            setMuscles(data.category);
          }
        })
        .catch((error) =>
          console.error('Error fetching exercise details:', error)
        );
    }
  }, [authTokens, id]);

  if (!exercise) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">{exercise.name}</h1>
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-2xl mx-auto">
        <img
          src={exercise.image}
          alt={exercise.name}
          className="w-full object-cover rounded-lg mb-6"
        />
        <h2 className="text-xl font-semibold mb-2">Description</h2>
        <p className="text-gray-700 mb-4">{exercise.description}</p>
        <h3 className="text-lg font-semibold mb-2">Starting Position</h3>
        <p className="text-gray-700 mb-4">{exercise.starting_position}</p>
        <h3 className="text-lg font-semibold mb-2">Execution</h3>
        <p className="text-gray-700">{exercise.execution}</p>

        {equipment.length > 0 && (
          <div>
            <h3 className="text-xl font-semibold text-gray-800 mb-2">
              Equipment Requirements
            </h3>
            <ul className="list-disc list-inside text-gray-600 text-lg">
              {equipment.map((equip) => (
                <li
                  key={equip.id}
                  className="ml-4"
                >
                  {equip.name}
                </li>
              ))}
            </ul>
          </div>
        )}

        {muscles.length > 0 && (
          <div>
            <h3 className="text-xl font-semibold text-gray-800 mb-2">
              Muscle Tags
            </h3>
            <ul className="list-disc list-inside text-gray-600 text-lg">
              {muscles.map((muscle) => (
                <li
                  key={muscle.id}
                  className="ml-4"
                >
                  {muscle.name}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default ExerciseItem;
