// 관리자 버튼
const adminbtn = document.getElementById("admin-btn");
const admincontent = document.querySelector(".admin-container");
const questform = document.querySelector(".formbox");
const istLogedBox = document.getElementById("isLoged");

adminbtn.addEventListener("click", function (e) {
  admincontent.classList.toggle("admin-container");
});

const questHandler = () => {
  admincontent.classList.toggle("admin-container");
  questform.classList.toggle("formbox");
};

const jquest = document.getElementById("jquest");
jquest.addEventListener("click", questHandler);
const jsquest = document.getElementById("jsquest");
jsquest.addEventListener("click", questHandler);
const jbquest = document.getElementById("jbquest");
jbquest.addEventListener("click", questHandler);
const jhquest = document.getElementById("jhquest");
jhquest.addEventListener("click", questHandler);

const cancelquest = document.getElementById("buttonc");
cancelquest.addEventListener("click", function () {
  questform.classList.toggle("formbox");
});

// emailjs 라이브러리 사용
const btn = document.getElementById("buttone");

document.getElementById("form").addEventListener("submit", function (event) {
  event.preventDefault();

  btn.value = "보내는 중...";

  const serviceID = "bam";
  const templateID = "template_c7kl71g";

  emailjs.sendForm(serviceID, templateID, this).then(
    () => {
      btn.value = "Send Email";
      alert("문의되었습니다.");
    },
    (err) => {
      btn.value = "Send Email";
      alert(JSON.stringify(err));
    }
  );
});

const logoutHandler = (event) => {
  $.ajax({
    type: "POST",
    url: "/api/logout",
    data: {},
    success: function (response) {
      if (response["result"] == "success") {
        console.log($);
        $.cookie("mytoken", response["token"]);

        window.location.href = "/";
      } else {
        // 로그아웃이 안되면
        alert("로그아웃이 실패했어요.");
      }
    },
  });
};


// 스크롤 내리면 서서히 커지는 애니메이션 효과
const saDefaultMargin = 300;
let saTriggerMargin = 0;
let saTriggerHeight = 0;
const saElementList = document.querySelectorAll('.sa');

const saFunc = function() {
  for (const element of saElementList) {
    if (!element.classList.contains('show')) {
      if (element.dataset.saMargin) {
        saTriggerMargin = parseInt(element.dataset.saMargin);
      } else {
        saTriggerMargin = saDefaultMargin;
      }

      if (element.dataset.saTrigger) {
        saTriggerHeight = document.querySelector(element.dataset.saTrigger).getBoundingClientRect().top + saTriggerMargin;
      } else {
        saTriggerHeight = element.getBoundingClientRect().top + saTriggerMargin;
      }

      if (window.innerHeight > saTriggerHeight) {
        let delay = (element.dataset.saDelay) ? element.dataset.saDelay : 0;
        setTimeout(function() {
          element.classList.add('show');
        }, delay);
      }
    }
  }
}

window.addEventListener('load', saFunc);
window.addEventListener('scroll', saFunc);