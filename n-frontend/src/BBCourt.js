import React from "react";
import { Link } from "react-router-dom";
import "./BBCourt.css";

function BBCourt() {
  return (
    <div className="Page">
      <div className="Detail_Container">
        <h1>BB Court : ใกล้เทคโนลาดกระบัง สนามบินสุวรรณภูมิ</h1>
        <p className="Address">ซ.ฉลองกรุง 1 ถ.ฉลองกรุง ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร</p>
        <div>
          <table className="Top_table">
            <tr>
              <th> {/*เบอร์โทร */}
                  <h4>เบอร์โทรติดต่อ : 0869822205</h4>
              </th>
              <th> {/*ราคา */}
                <h2>ค่าเช่า</h2>
                <h4>ราคา 4,700 บาท/เดือน</h4>
              </th>
            </tr>
          </table>
        </div>
        <div className="Dor_photo">
          <table>
            <tr>
              <td>
                <img src={`images/BBCourt_pic.jpg`}/>
              </td>
              <td>
                <h2>รายละเอียด</h2>
                <p>ห้องพักราคาสบายกระเป๋า อยู่ใกล้ สถาบันเทคโนโลยีเจ้าคุณทหารลาดกระบัง
                  และสนามบินสุวรรณภูมิ เหมาะสำหรับนักศึกษา Free Cable TV ทุกห้อง
                  มากกว่า 100 ช่อง Free ที่จอดรถจักรยาน, มอเตอร์ไซค์ในร่ม
                  ระบบรักษาความปลอดภัย เข้า - ออก ด้วยระบบ Keycard และกล้อง CCTV ทั่วบริเวณ
                  บันทึก 24 ชม.บริการร้านมินิมาร์ทในโครงการ อาหารตามสั่ง มีบริการเครื่องซักผ้า ทุกชั้น!! เฟอนิเจอร์ครบชุด ภายในห้องมี
                  เตียงพร้อมฟูก ขนาด 5 ฟุต โต๊ะเขียนหนังสือพร้อมเก้าอี้ 2 ชุด แอร์ ผ้าม่าน มุ้งลวด ตู้เสื้อผ้า โต๊ะวาง TV โต๊ะเครื่องแป้งพร้อมเก้าอี้
                  สามารถพักได้ 2 คน สบายๆ ราคาสบายกระเป๋า!!</p>
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
              <td>4,700 บาท/เดือน</td>
              <td>1 เดือน</td>
              <td>1 เดือน</td>
              <td>8 บาท/ยูนิต</td>
              <td>16 บาท/ยูนิต</td>
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
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>พัดลม</tr>
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
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ที่จอดรถมอเตอร์ไซต์ / จักรยาน</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ลิฟต์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สระว่ายน้ำ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โรงยิม/ฟิตเนส</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>อินเตอร์เน็ตไร้สาย (WIFI) ในห้อง</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>เคเบิลทีวี / ดาวเทียม</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>มีระบบรักษาความปลอดภัย (keycard)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มีระบบรักษาความปลอดภัย (สแกนลายนิ้วมือ)</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>กล้องวงจรปิด (CCTV)</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>รปภ.</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านขายอาหาร</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านค่า ร้านสะดวกซื้อ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านซัก-รีด / มีบริการเครื่องซักผ้า</tr>
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

export default BBCourt;