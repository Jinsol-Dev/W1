// 관리자 버튼
const adminbtn = document.getElementById('admin-btn')
const admincontent = document.querySelector('.admin-container')
const questform = document.querySelector('.formbox')
const istLogedBox = document.getElementById('isLoged')

$(document).ready(function () {
  if (document.cookie === '') {
    istLogedBox.innerHTML = `<a class="nav-link text-uppercase" href="/login"> 로그인 </a>`
  } else {
    const logoutbtn = document.createElement('button')
    logoutbtn.className = 'nav-link'
    logoutbtn.classList.add('text-uppercase')
    logoutbtn.setAttribute('id', 'nickOut')
    logoutbtn.innerText = '로그아웃'
    logoutbtn.addEventListener('click', logoutHandler)
    istLogedBox.appendChild(logoutbtn)
    // logoutbtn.istLogedBox.innerHTML = `<button class="nav-link text-uppercase" id='nickOut'> 로그아웃 </button>`
  }
})

adminbtn.addEventListener('click', function (e) {
  admincontent.classList.toggle('admin-container')
})

const questHandler = () => {
  admincontent.classList.toggle('admin-container')
  questform.classList.toggle('formbox')
}

const jquest = document.getElementById('jquest')
jquest.addEventListener('click', questHandler)
const jsquest = document.getElementById('jsquest')
jsquest.addEventListener('click', questHandler)
const jbquest = document.getElementById('jbquest')
jbquest.addEventListener('click', questHandler)
const jhquest = document.getElementById('jhquest')
jhquest.addEventListener('click', questHandler)

const cancelquest = document.getElementById('buttonc')
cancelquest.addEventListener('click', function () {
  questform.classList.toggle('formbox')
})

// emailjs 라이브러리 사용
const btn = document.getElementById('buttone')

document.getElementById('form').addEventListener('submit', function (event) {
  event.preventDefault()

  btn.value = '보내는 중...'

  const serviceID = 'bam'
  const templateID = 'template_c7kl71g'

  emailjs.sendForm(serviceID, templateID, this).then(
    () => {
      btn.value = 'Send Email'
      alert('문의되었습니다.')
    },
    (err) => {
      btn.value = 'Send Email'
      alert(JSON.stringify(err))
    },
  )
})

const logoutHandler = (event) => {
  $.ajax({
    type: 'POST',
    url: '/api/logout',
    data: {},
    success: function (response) {
      if (response['result'] == 'success') {
        console.log($)
        $.cookie('mytoken', response['token'])

        window.location.href = '/'
      } else {
        // 로그아웃이 안되면
        alert('로그아웃이 실패했어요.')
      }
    },
  })
}
