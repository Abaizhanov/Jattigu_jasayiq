import { useContext, useState } from 'react';
import { Dialog } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';
import { Link } from 'react-router-dom'; // Use react-router for navigation
import logo from '../assets/logo.jpg';
import AuthContext from '../context/AuthContext';
import swal from 'sweetalert2';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const { user, logoutUser } = useContext(AuthContext);
  const history = useHistory();

  async function handleLogout() {
    try {
      await logoutUser();
      swal.fire('Success', 'Logged out successfully', 'success');
      history.push('/');
    } catch (error) {
      swal.fire('Error', 'Invalid', 'error');
    }
  }
  return (
    <header className="relative bg-white">
      {/* <div className="bg-gray-900 w-[470px] h-[1050px] absolute right-0 top-[-200px] z-[0]" /> */}

      <nav
        aria-label="Global"
        className="relative mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8 z-10"
      >
        <div className="flex lg:flex-1">
          <Link
            to="/"
            className="-m-1.5 p-1.5"
          >
            <span className="sr-only">Your Company</span>
            <img
              alt="Your Company"
              src={logo}
              className="h-8 w-auto"
            />
          </Link>
        </div>
        <div className="flex lg:hidden">
          <button
            type="button"
            onClick={() => setMobileMenuOpen(true)}
            className="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          >
            <span className="sr-only">Open main menu</span>
            <Bars3Icon
              className="h-6 w-6"
              aria-hidden="true"
            />
          </button>
        </div>
        <div className="hidden lg:flex lg:gap-x-12">
          <Link
            to="/"
            className="text-sm font-semibold leading-6 text-gray-900"
          >
            Home
          </Link>
          <Link
            to="/about"
            className="text-sm font-semibold leading-6 text-gray-900"
          >
            About
          </Link>
          <Link
            to="/exercises"
            className="text-sm font-semibold leading-6 text-gray-900"
          >
            Exercises
          </Link>
          <Link
            to="/nutritions"
            className="text-sm font-semibold leading-6 text-gray-900"
          >
            Nutritions
          </Link>
          <Link
            to="/blog"
            className="text-sm font-semibold leading-6 text-gray-900"
          >
            Blog
          </Link>
        </div>
        <div className="hidden lg:flex lg:flex-1 lg:justify-end z-[1]">
          {!user ? (
            <Link
              to="/login"
              className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-white hover:bg-gray-50 "
            >
              Log in
            </Link>
          ) : (
            <Link
              to="/"
              onClick={handleLogout}
              className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-red-700 hover:bg-gray-50 "
            >
              Logout
            </Link>
          )}
        </div>
      </nav>
      <Dialog
        open={mobileMenuOpen}
        onClose={() => setMobileMenuOpen(false)}
        className="lg:hidden"
      >
        <div className="fixed inset-0 z-10" />
        <Dialog.Panel className="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div className="flex items-center justify-between">
            <Link
              to="/"
              className="-m-1.5 p-1.5"
            >
              <span className="sr-only">Your Company</span>
              <img
                alt="Your Company"
                src="/logo.jpg"
                className="h-8 w-auto"
              />
            </Link>
            <button
              type="button"
              onClick={() => setMobileMenuOpen(false)}
              className="-m-2.5 rounded-md p-2.5 text-gray-700"
            >
              <span className="sr-only">Close menu</span>
              <XMarkIcon
                className="h-6 w-6"
                aria-hidden="true"
              />
            </button>
          </div>
          <div className="mt-6 flow-root">
            <div className="-my-6 divide-y divide-gray-500/10">
              <div className="space-y-2 py-6">
                <Link
                  to="/"
                  className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  Home
                </Link>
                <Link
                  to="/about"
                  className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  About
                </Link>
                <Link
                  to="/exercises"
                  className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  Exercises
                </Link>
                <Link
                  to="/nutritions"
                  className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  Nutritions
                </Link>
                <Link
                  to="/blog"
                  className="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  Blog
                </Link>
              </div>
              <div className="py-6">
                {!user ? (
                  <Link
                    to="/login"
                    className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-orange-900 hover:bg-gray-50 "
                  >
                    Log in
                  </Link>
                ) : (
                  <Link
                    to="/"
                    onClick={handleLogout}
                    className="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-rose-950 hover:bg-gray-50 "
                  >
                    Logout
                  </Link>
                )}
              </div>
            </div>
          </div>
        </Dialog.Panel>
      </Dialog>
    </header>
  );
}
