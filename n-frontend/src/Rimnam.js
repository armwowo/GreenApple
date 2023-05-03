import React from "react";
import { Link } from "react-router-dom";
import "./Rimnam.css";

function Rimnam() {
  return (
    <div className="Page">
      <div className="Detail_Container">
        <h1>หอริมน้ำ</h1>
        <p className="Address">ซ.ลาดกระบัง 13/5 ถ.อ่อนนุช-ลาดกระบัง กรุงเทพมหานคร</p>
        <div>
          <table className="Top_table">
            <tr>
              <th> {/*เบอร์โทร */}
                  <h4>เบอร์โทรติดต่อ : 0816972604</h4>
              </th>
              <th> {/*ราคา */}
                <h2>ค่าเช่า</h2>
                <h4>ราคา 6,000 บาท/เดือน</h4>
                <h4>ราคา 990 บาท/เดือน</h4>
              </th>
            </tr>
          </table>
        </div>
        <div className="Dor_photo">
          <table>
            <tr>
              <td>
                <img src={`images/rimnam_pic.jpg`}/>
              </td>
              <td>
                <h2>รายละเอียด</h2>
                <p>หอริมน้ำไม่อนุญาตเลี้ยงสัตว์ หอใหม่ซอยลาดกระบัง 13/8 ห้องว่างให้เช่าหอริมน้ำใกล้สนามบินสุวรรณภูมิและเทคโนพระจอมเกล้าลาดกระบัง สามารถเดินไปเทคโนลาดกระบังได้ เดินเข้าคณะเกษตรและฟู้ดซายด์ได้
                    หอริมน้ำใกล้สนามบินสุวรรณภูมิ ซอยลาดกระบัง 13/5 ( ซอยท๊อปซุปเปอร์คุ้ม) ฝั่งตรงข้ามเป็นซอยลาดกระบัง 51
                    ติด FBT fitness เดินลงมาสามารถเข้า fitness ได้เลย บริเวณติดกันคือร้านอาหาร
                    และห้างสรรพสินค้าท๊อป ไม่เปรี่ยว ของกินเพียบ สามารถเดินไปเทคโนพระจอมเกล้าลาดกระบัง คณะเกษตรได้ 
                    ใกล้ปากทางเข้าสนามบินสุวรรณภูมิ แยกสุขสมาน สามารถเดินไปขึ้นรถตู้ที่แยกสุขสมานได้
                    ผู้เช่าส่วนใหญ่ได้แก่ นักศึกษาเทคโนพระจอมเกล้าลาดกระบัง นักศึกษาวิทยาลัยช่างศิลป์ และ พนักงานสนามบินสุวรรณภูมิ
                    สนใจ tel: 081-697-2604 , ID line: 0816972604 (โทรได้ 8.00-19.00น. หลัง 1 ทุ่ม กรุณาไลน์ฝากข้อความไว้)
                    สถานีที่ใกล้เคียง: สนามบินสุวรรณภูมิ, เทคโนพระจอมเกล้าลาดกระบัง, โรงพยาบาลลาดกระบัง, สำนักงานเขตลาดกระบัง, แยกสุขสมาน, สวนพระนคร
                </p>
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
              <td>6,000 บาท/เดือน</td>
              <td>1 เดือน</td>
              <td>1 เดือน</td>
              <td>8 บาท/ยูนิต</td>
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
              <tr className="False">
                <img src={`images/check_no.jpg`}/>เครื่องทำน้ำอุ่น</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>พัดลม</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>มี TV ให้</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ตู้เย็น</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>โทรศัพท์สายตรง</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>อนุญาตให้เลี้ยงสัตว์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>อนุญาตให้สูบบุหรี่ในหอพัก</tr>
            </td>
            <td>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ที่จอดรถ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ที่จอดรถมอเตอร์ไซต์ / จักรยาน</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ลิฟต์</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>สระว่ายน้ำ</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>โรงยิม/ฟิตเนส</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>อินเตอร์เน็ตไร้สาย (WIFI) ในห้อง</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>เคเบิลทีวี / ดาวเทียม</tr>
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
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านค่า ร้านสะดวกซื้อ</tr>
              <tr className="False">
                <img src={`images/check_no.jpg`}/>ร้านซัก-รีด / มีบริการเครื่องซักผ้า</tr>
              <tr className="True">
                <img src={`images/check_mark.jpg`}/>ร้านทำผม-เสริมสวย</tr>
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

export default Rimnam;