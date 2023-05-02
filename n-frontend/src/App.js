import Navbar from "./Navbar"
import Home from "./Home"
import Login from "./Login"
import Register from "./Register"
import Sabaiplace from "./สบายเพลส"
import Reserve from "./Reserve"
import APPLEHOUSE from "./APPLEHOUSE"
import AdCha from "./อัจฉริยา"
import Bankum from "./บ้านคุ้มเกล้า48"
import BBCourt from "./BBCourt"
import APHouse from "./APHouse"
import Buri from "./บุรีไอริส"
import Allsmile from "./ออลสมายล์"
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
          <Route path="/APPLEHOUSE" element={<APPLEHOUSE/>} />
          <Route path="/อัจฉริยา" element={<AdCha/>} />
          <Route path="/บ้านคุ้มเกล้า48" element={<Bankum/>} />
          <Route path="/BBCourt" element={<BBCourt/>} />
          <Route path="/APHouse" element={<APHouse/>} />
          <Route path="/บุรีไอริส" element={<Buri/>} />
          <Route path="/ออลสมายล์" element={<Allsmile/>} />
          <Route path="/Reserve" element={<Reserve/>} />
        </Routes>
      </div>
    </>
  )
}

export default App