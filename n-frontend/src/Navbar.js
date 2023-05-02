import { useState } from 'react';
import { Link, useMatch, useResolvedPath } from 'react-router-dom';

export default function Navbar() {
  const [searchValue, setSearchValue] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const dorms = [
    { id: 1, name: "สบายเพลส", address: "ถ.ฉลองกรุง ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร", price: 4500 },
    { id: 2, name: "Dorm B", address: "789/012 Road, Bangkok", price: 2500 },
    { id: 3, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 4, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 5, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 6, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 7, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 8, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 9, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
    { id: 10, name: "Dorm C", address: "345/678 Road, Bangkok", price: 2000 },
  ];

  const handleSearch = async () => {
    const response = await fetch(`http://127.0.0.1:8000/searchByName?name=${searchValue}`);
    const data = await response.json();
    setSearchResults(data['Dormitory Catalog']);
  };

  const handleSearchInputChange = (event) => {
    setSearchValue(event.target.value);
  };

  return (
    <nav className="nav">
      <Link to="/" className="site-title">
        RentHub
      </Link>
      <ul>
        <CustomLink to="/">Home</CustomLink>
        <CustomLink to="/Login">Login</CustomLink>
        <CustomLink to="/Register">Register</CustomLink>
        <li>
          <input type="text" value={searchValue} onChange={handleSearchInputChange} placeholder="Search dormitory" />
          <button onClick={handleSearch}>Search</button>
          {searchResults.length > 0 && (
            <ul>
              {searchResults.map((dormitory) => (
                <li key={dormitory.id}>
                  <Link to={`/${dormitory.name}`}>{dormitory.name}</Link>
                </li>
              ))}
            </ul>
          )}
        </li>
      </ul>
    </nav>
  );
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}
