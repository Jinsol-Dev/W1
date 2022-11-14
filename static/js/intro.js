// 관리자 버튼
const adminbtn = document.getElementById('admin-btn')
const admincontent = document.querySelector('.admin-container')
console.log(adminbtn)

adminbtn.addEventListener('click', function (e) {
  console.log(admincontent)
  admincontent.classList.toggle('admin-container')
})
