import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faFacebook,
  faTwitter,
  faInstagram,
  faLinkedin,
} from '@fortawesome/free-brands-svg-icons';

const footerLinks = [
  { name: 'Home', href: '#' },
  { name: 'About Us', href: '#' },
  { name: 'Services', href: '#' },
  { name: 'Blog', href: '#' },
  { name: 'Contact', href: '#' },
];

const contactInfo = {
  address: '123 Fitness St, Suite 456',
  cityStateZip: 'City, State, ZIP',
  email: 'info@example.com',
  phone: '(123) 456-7890',
};

const socialLinks = [
  { icon: faFacebook, href: '#', name: 'Facebook' },
  { icon: faTwitter, href: '#', name: 'Twitter' },
  { icon: faInstagram, href: '#', name: 'Instagram' },
  { icon: faLinkedin, href: '#', name: 'LinkedIn' },
];

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-white py-10">
      <div className="container mx-auto px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              {footerLinks.map((link) => (
                <li key={link.name}>
                  <a
                    href={link.href}
                    className="hover:underline"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact Us</h3>
            <p className="mb-2">{contactInfo.address}</p>
            <p className="mb-2">{contactInfo.cityStateZip}</p>
            <p className="mb-2">Email: {contactInfo.email}</p>
            <p className="mb-2">Phone: {contactInfo.phone}</p>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Follow Us</h3>
            <div className="flex space-x-4">
              {socialLinks.map((link) => (
                <a
                  key={link.name}
                  href={link.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-gray-400 hover:text-white"
                  aria-label={link.name}
                >
                  <FontAwesomeIcon
                    icon={link.icon}
                    className="h-6 w-6"
                  />
                </a>
              ))}
            </div>
          </div>
        </div>
        <div className="mt-10 border-t border-gray-700 pt-4 text-center">
          <p className="text-sm text-gray-400">
            &copy; {new Date().getFullYear()} Your Company Name. All rights
            reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
