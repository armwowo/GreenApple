import React from "react";
import { Link } from "react-router-dom";
import "./APHouse.css";


{/*แก้ข้อมูล */}

function APHouse() {
  return (
    <div className="Page">
      <div className="Detail_Container">
        <h1>AP House</h1>
        <p className="Address">ซ.เกกีงาม 1 ถ.ฉลองกรุง 1 ลาดกระบัง ลาดกระบัง กรุงเทพมหานคร</p>
        <div>
          <table className="Top_table">
            <tr>
              <th> {/*เบอร์โทร */}
                  <h4>เบอร์โทรติดต่อ : 0819224669</h4>
              </th>
              <th> {/*ราคา */}
                <h2>ค่าเช่า</h2>
                <h4>ราคา 5,300 บาท/เดือน</h4>
              </th>
            </tr>
          </table>
        </div>
        <div className="Dor_photo">
          <table>
            <tr>
              <td>
                <img src={`images/aphouse_pic.jpg`}/>
              </td>
              <td>
                <h2>รายละเอียด</h2>
                <p>หอพักชาย อาคารปูนเปลือย Style modern อาคารติดคณะวิศวะพระจอมเกล้าลาดกระบัง ซอยแรก
                    สามารถเดินไปเรียนได้ใน 5 นาที ห่างจากสนามบินสุวรรณภูมิ 15 นาที ภูมทัศน์รอบอาคารโปร่ง
                    ล้อมด้วยต้นไม้ร่มรื่น ใกล้คลอง ลมถ่ายเทตลอดวันมีที่จอดรดจักรยานและมอเตอร์ไซด์ในร่ม ภายในรั้ว
                    finger scan ผู้เช่าจอดมอเตอร์ไซด์ในร่ม ภายในรั้ว ฟรี ห้องละ 1 คัน บริการเครื่องซ้กผ้าหยอดเหรียญ
                    บริการเครื่องอบผ้า หยอดเหรียญ พักห้องละ 1 ท่าน ความปลอดภัย ปลอดภัยด้วยกล้องวงจรปิดทุกชั้น
                    รอบอาคารและที่จอดรถจักรยานยนต์รั้วรอบอาคาร เข้าออกอาคาร  finger scan
                    และ ประตูรั้วด้วย key card ทุกห้องประกอบด้วย แอร์ Mr. Slim ล้างแอร์ฟรีทุกปี
                    เฟอร์นิเจอร์ครบ ตู้เสื้อผ้าขนาดใหญ่ เตียง ที่นอน 6 ฟุต คิงค์ไซด์ ชุดโต็ะเก้าอี้เขียนหนังสือ ประตูระเบียงกระจก ม่าน ราวตากผ้า
                    ทุกห้องมีระเบียงส่วนต้ว ห้องน้ำ ในตัว High speed internet ห้องละ 35/30 - 45/40 Mbps WIFI + LAN ฟรี เครื่องทำน้ำอุ่น
                    สัญญาณดาวเทียม<br/></p>
                <h5>*** หอพักปลอดของมึนเมาและสารเสพติด ขออนุญาตรับเฉพาะผู้พักที่ไม่ดื่มของมึนเมา ไม่สูบบุหรี่</h5>
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
              <td>5,300 บาท/เดือน</td>
              <td>1 เดือน</td>
              <td>1 เดือน</td>
              <td>7 บาท/ยูนิต</td>
              <td>14 บาท/ยูนิต</td>
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
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>มี TV ให้</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ตู้เย็น</tr>
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
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มีระบบรักษาความปลอดภัย (keycard)</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>มีระบบรักษาความปลอดภัย (สแกนลายนิ้วมือ)</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>กล้องวงจรปิด (CCTV)</tr>
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

export default APHouse;