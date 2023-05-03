import React, { useState, useEffect } from 'react';
import "./Searchbar.css";

function SearchBar() {
  const [searchTerm, setSearchTerm] = useState('');
  const [dormitoryList, setDormitoryList] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/firstpagedata`)
      .then(response => response.json())
      .then(data => {
        setDormitoryList(data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleInputChange = event => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = () => {
    const filteredDormitoryList = dormitoryList.filter(
      dormitory =>
        dormitory.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    console.log(filteredDormitoryList); // แสดงผลลัพธ์ใน console
  };

  return (
    <div className='Search_container'>
        <input type="text" value={searchTerm} onChange={handleInputChange} />  
        <button onClick={handleSearch}>Search</button>
    </div>
  );
}

export default SearchBar;
