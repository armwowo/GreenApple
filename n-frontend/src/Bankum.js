import React from "react";
import { Link } from "react-router-dom";
import "./Bankum.css";

function Bankum() {
  return (
    <div className="Page">
      <div className="Detail_Container">
        <h1>บ้านคุ้มเกล้า 48</h1>
        <p className="Address">ซ.48 ถ.คุ้มเกล้า ลำปลาทิว ลาดกระบัง กรุงเทพมหานคร</p>
        <div>
          <table className="Top_table">
            <tr>
              <th> {/*เบอร์โทร */}
                  <h4>เบอร์โทรติดต่อ : 0814456427</h4>
                  <h4>หรือเบอร์ : 0897981157</h4>
              </th>
              <th> {/*ราคา */}
                <h2>ค่าเช่า</h2>
                <h4>ราคา 5,000 บาท/เดือน</h4>
              </th>
            </tr>
          </table>
        </div>
        <div className="Dor_photo">
          <table>
            <tr>
              <td>
                <img src={`images/Bankum_pic.jpg`}/>
              </td>
              <td>
                <h2>รายละเอียด</h2>
                <p>บ้านพักสไตล์รีสอร์ต ให้เช่ารายเดือน (สัญญา12เดือน) กว้าง4*ลึก6เมตร<br/>
                  ขนาดห้อง24ตรม.(ไม่รวมระเบียง) มีระเบียงด้านหน้าบ้าน พร้อมที่จอดรถยนต์ส่วนตัว<br/>
                  ด้านข้างมีหลังคา ภายในห้องมี แอร์1ตัว(13000BTU) ห้องน้ำในตัว เครื่องทำน้ำอุ่น<br/>
                  อ่างล้างจาน ห้ามเลี้ยงสัตว์ในห้องพัก ห้ามสูบบุหรี่ในห้องพัก</p>
                <button>สถานะ :</button>
              </td>
            </tr>
          </table>
        </div>
        <div className="Detail_table">
          <h2>ตารางค่าใช้จ่าย</h2>
          <table>
            <tr>
              <th>รายเดือน</th>
              <th>เงินประกัน</th>
              <th>จ่ายล่วงหน้า</th>
              <th>ค่าไฟ</th>
              <th>ค่าน้ำ</th>
            </tr>
            <tr>
              <td>5,000 บาท/เดือน</td>
              <td>5,000 บาท</td>
              <td>1 เดือน</td>
              <td>7 บาท/ยูนิต</td>
              <td>18 บาท/ยูนิต</td>
            </tr>
          </table>
        </div>
        <div className="Facility">
          <h2>สิ่งอำนวยความสะดวก:</h2>
          <table>
            <td>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เครื่องปรับอากาศ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เฟอร์นิเจอร์-ตู้ เตียง</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เครื่องทำน้ำอุ่น</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>พัดลม</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มี TV ให้</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ตู้เย็น</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โทรศัพท์สายตรง</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อนุญาตให้เลี้ยงสัตว์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อนุญาตให้สูบบุหรี่ในหอพัก</tr>
            </td>
            <td>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ที่จอดรถ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ที่จอดรถมอเตอร์ไซต์ / จักรยาน</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ลิฟต์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สระว่ายน้ำ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โรงยิม/ฟิตเนส</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อินเตอร์เน็ตไร้สาย (WIFI) ในห้อง</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>เคเบิลทีวี / ดาวเทียม</tr>
              <tr className="Fslae">
                <img src={`images/check_no.jpg`}/>มีระบบรักษาความปลอดภัย (keycard)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มีระบบรักษาความปลอดภัย (สแกนลายนิ้วมือ)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>กล้องวงจรปิด (CCTV)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>รปภ.</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านขายอาหาร</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านค่า ร้านสะดวกซื้อ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านซัก-รีด / มีบริการเครื่องซักผ้า</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านทำผม-เสริมสวย</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สถานี charge รถไฟฟ้า</tr>
            </td>
          </table>
        </div>
        <Link to={`/Reserve`}>
          <button className="Reserve">จองห้องพัก</button>
        </Link>
      </div>
    </div>
  );
}

export default Bankum;