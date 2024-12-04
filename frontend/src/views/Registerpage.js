import { useState, useContext } from 'react';
import { Link, useHistory } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import logo from '../assets/logo_regis.jpg';

function Registerpage() {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('Male'); // Default value
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [fitnessGoal, setFitnessGoal] = useState('Lose Weight'); // Default value

  const { registerUser } = useContext(AuthContext);
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Ensure numeric fields are integers
    const parsedAge = parseInt(age, 10);
    const parsedWeight = parseInt(weight, 10);
    const parsedHeight = parseInt(height, 10);

    // Call the registerUser function with properly formatted inputs
    await registerUser(
      email,
      username,
      password,
      password2,
      parsedAge,
      gender,
      parsedWeight,
      parsedHeight,
      fitnessGoal
    );
  };

  return (
    <div>
      <section className="min-h-screen bg-gray-200 flex items-center justify-center">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-5xl mx-auto bg-white rounded-lg shadow-lg">
            <div className="grid grid-cols-1 md:grid-cols-2">
              <div className="hidden md:block">
                <img
                  src={logo}
                  alt="login form"
                  className="h-full w-full object-cover rounded-l-lg"
                />
              </div>
              <div className="flex items-center">
                <div className="p-8 w-full">
                  <form onSubmit={handleSubmit}>
                    <div className="text-center mb-6">
                      <h2 className="text-2xl font-bold text-gray-800">
                        Welcome to <b>Desphixs 👋</b>
                      </h2>
                      <p className="text-gray-600">Sign Up</p>
                    </div>
                    <div className="space-y-4">
                      <input
                        type="email"
                        placeholder="Email Address"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                      />
                      <input
                        type="text"
                        placeholder="Username"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                      />
                      <input
                        type="password"
                        placeholder="Password"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                      />
                      <input
                        type="password"
                        placeholder="Confirm Password"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={password2}
                        onChange={(e) => setPassword2(e.target.value)}
                      />
                      <input
                        type="number"
                        placeholder="Age"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={age}
                        onChange={(e) => setAge(e.target.value)}
                      />
                      <select
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={gender}
                        onChange={(e) => setGender(e.target.value)}
                      >
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                      </select>
                      <input
                        type="number"
                        placeholder="Weight (kg)"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={weight}
                        onChange={(e) => setWeight(e.target.value)}
                      />
                      <input
                        type="number"
                        placeholder="Height (cm)"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                      />
                      <select
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        value={fitnessGoal}
                        onChange={(e) => setFitnessGoal(e.target.value)}
                      >
                        <option value="Lose Weight">Lose Weight</option>
                        <option value="Build Muscle">Build Muscle</option>
                        <option value="Stay Fit">Stay Fit</option>
                      </select>
                    </div>
                    <button
                      type="submit"
                      className="w-full bg-indigo-600 text-white p-3 rounded-lg mt-6 hover:bg-indigo-700"
                    >
                      Register
                    </button>
                    <div className="text-center mt-4 text-gray-600">
                      Already have an account?{' '}
                      <Link
                        to="/login"
                        className="text-indigo-500"
                      >
                        Login Now
                      </Link>
                    </div>
                  </form>
                  <div className="text-center mt-4 text-sm text-gray-500">
                    <a
                      href="#!"
                      className="hover:underline"
                    >
                      Terms of use
                    </a>{' '}
                    |{' '}
                    <a
                      href="#!"
                      className="hover:underline"
                    >
                      Privacy policy
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Registerpage;
