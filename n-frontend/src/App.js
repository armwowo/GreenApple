import Navbar from "./Navbar"
import Home from "./Home"
import Login from "./Login"
import Register from "./Register"
import Sabaiplace from "./สบายเพลส"
import Reserve from "./Reserve"
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <>
      <Navbar />
      <div>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/Login" element={<Login/>} />
          <Route path="/Register" element={<Register/>} />
          <Route path="/สบายเพลส" element={<Sabaiplace/>} />
          <Route path="/Reserve" element={<Reserve/>} />
        </Routes>
      </div>
    </>
  )
}

export default App