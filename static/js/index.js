console.log('hi')
const test = document.getElementById('testbtn')
test.addEventListener('click', save_test)

function save_test() {
  console.log('hi')
  $.ajax({
    type: 'POST',
    url: '/',
    data: { box_give: 'hi' },
    success: function (response) {
      console.log(response['msg'])
      window.location.reload()
    },
  })
}
