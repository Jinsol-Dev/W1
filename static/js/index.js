const test = document.getElementById('testbtn')
test.addEventListener('click', save_test)

function save_test() {
  $.ajax({
    type: 'get',
    url: '/namyang/hospital',
    data: { box_give: 'hi' },
    success: function (response) {
      console.log(response['msg'])
      window.location.reload()
    },
  })
}
