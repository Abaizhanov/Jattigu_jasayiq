import { useState, useEffect } from 'react';
import useAxios from '../utils/useAxios';
import jwtDecode from 'jwt-decode';

function Dashboard() {
  const [res, setRes] = useState('');
  const api = useAxios();
  const token = localStorage.getItem('authTokens');

  if (token) {
    const decode = jwtDecode(token);
    var user_id = decode.user_id;
    var username = decode.username;
    var full_name = decode.full_name;
    var image = decode.image;
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get('/test/');
        setRes(response.data.response);
      } catch (error) {
        console.log(error);
        setRes('Something went wrong');
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    const fetchPostData = async () => {
      try {
        const response = await api.post('/test/');
        setRes(response.data.response);
      } catch (error) {
        console.log(error);
        setRes('Something went wrong');
      }
    };
    fetchPostData();
  }, []);

  return (
    <div>
      <div className="container mx-auto pt-24">
        <div className="flex">
          <nav className="w-1/4 bg-gray-100 p-4 rounded-lg shadow-md mt-4">
            <div className="space-y-4">
              <ul className="space-y-2">
                <li>
                  <a
                    className="text-blue-500 hover:text-blue-700"
                    href="#"
                  >
                    Dashboard
                  </a>
                </li>
                <li>
                  <a
                    className="text-gray-700 hover:text-gray-900"
                    href="#"
                  >
                    Orders
                  </a>
                </li>
                <li>
                  <a
                    className="text-gray-700 hover:text-gray-900"
                    href="#"
                  >
                    Products
                  </a>
                </li>
                <li>
                  <a
                    className="text-gray-700 hover:text-gray-900"
                    href="#"
                  >
                    Customers
                  </a>
                </li>
                <li>
                  <a
                    className="text-gray-700 hover:text-gray-900"
                    href="#"
                  >
                    Reports
                  </a>
                </li>
                <li>
                  <a
                    className="text-gray-700 hover:text-gray-900"
                    href="#"
                  >
                    Integrations
                  </a>
                </li>
              </ul>
              <div className="mt-8">
                <h6 className="font-semibold text-gray-500">Saved reports</h6>
                <ul className="space-y-2 mt-2">
                  <li>
                    <a
                      className="text-gray-700 hover:text-gray-900"
                      href="#"
                    >
                      Current month
                    </a>
                  </li>
                  <li>
                    <a
                      className="text-gray-700 hover:text-gray-900"
                      href="#"
                    >
                      Last quarter
                    </a>
                  </li>
                  <li>
                    <a
                      className="text-gray-700 hover:text-gray-900"
                      href="#"
                    >
                      Social engagement
                    </a>
                  </li>
                  <li>
                    <a
                      className="text-gray-700 hover:text-gray-900"
                      href="#"
                    >
                      Year-end sale
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </nav>

          <main className="w-3/4 pl-8">
            <div className="flex justify-between items-center pb-4 mb-3 border-b">
              <h1 className="text-2xl font-semibold">My Dashboard</h1>
              <span>Hello, {username}!</span>
              <div className="flex space-x-2">
                <button className="px-4 py-2 text-sm font-semibold text-white bg-blue-500 rounded hover:bg-blue-600">
                  Share
                </button>
                <button className="px-4 py-2 text-sm font-semibold text-white bg-blue-500 rounded hover:bg-blue-600">
                  Export
                </button>
              </div>
            </div>

            <div className="bg-green-100 p-4 rounded-lg mb-4">
              <strong>{res}</strong>
            </div>

            <h2 className="text-xl font-semibold mb-4">Section title</h2>

            <div className="overflow-x-auto">
              <table className="min-w-full table-auto">
                <thead>
                  <tr className="bg-gray-100">
                    <th className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                      #
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                      Header
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                      Header
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                      Header
                    </th>
                    <th className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                      Header
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {/* Sample Data */}
                  <tr className="border-b">
                    <td className="px-4 py-2">1,001</td>
                    <td className="px-4 py-2">Lorem</td>
                    <td className="px-4 py-2">ipsum</td>
                    <td className="px-4 py-2">dolor</td>
                    <td className="px-4 py-2">sit</td>
                  </tr>
                  <tr className="border-b">
                    <td className="px-4 py-2">1,002</td>
                    <td className="px-4 py-2">amet</td>
                    <td className="px-4 py-2">consectetur</td>
                    <td className="px-4 py-2">adipiscing</td>
                    <td className="px-4 py-2">elit</td>
                  </tr>
                  {/* Add more rows as needed */}
                </tbody>
              </table>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;