import Navbar from "./Navbar"
import Home from "./Home"
import Login from "./Login"
import Register from "./Register"
import Sabaiplace from "./Sabaiplace"
import UserProfile from "./components/Profile"
import Detail from "./components/Detail"
import { Route, Routes } from "react-router-dom"
import "./App.css"

function App() {
  
  return (
    <>
    <Navbar />
    <div classN ame="container">
      
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/Register" element={<Register />} />
          <Route path="/Sabaiplace" element={<Sabaiplace />} />
          <Route path="/Profile" element={<UserProfile />} />
          <Route path = "/Detail" element={<Detail />} />
        </Routes>
      </div>
    </>
  )
}

export default App