// 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })

var mapContainer = document.getElementById('map'), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
  }

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption)

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places()

// 키워드로 장소를 검색합니다
ps.keywordSearch('서울시 동물병원', placesSearchCB)

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    var bounds = new kakao.maps.LatLngBounds()

    for (var i = 0; i < data.length; i++) {
      displayMarker(data[i])
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds)
  }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
  // 마커를 생성하고 지도에 표시합니다
  var marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  })

  // 마커에 클릭이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'click', function () {
    // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
    infowindow.setContent(
      '<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>',
    )
    infowindow.open(map, marker)
  })
}

function show_pethospital() {
  $.ajax({
    type: 'GET',
    url: '/seoul_get',
    data: {},
    success: function (response) {
      console.log(response)
      let rows = response['pethospital']
      const bigContainer = document.getElementById('list')
      for (let i = 0; i < rows.length; i++) {
        let name = rows[i]['name']
        let cafeId = rows[i]['_id']
        let time = rows[i]['time']
        let phone = rows[i]['phone']
        let address = rows[i]['address']

        const cafeContainer = document.createElement('tr')
        cafeContainer.className = 'cafeList'
        cafeContainer.setAttribute('id', cafeId)
        cafeContainer.addEventListener('click', showModal)
        cafeContainer.innerHTML = `
        <th scope="row">병원</th>
        <td>${name}</td>
        <td>${time}</td>
        <td>${phone}</td>
                        <td>${address}</td>

                        `

        bigContainer.appendChild(cafeContainer)
      }
    },
  })
}

function showModal(e) {
  const cafeId = e.target.parentNode.id
  $.ajax({
    type: 'GET',
    url: `/get/seoul/${cafeId}`,
    data: {},
    success: function (response) {
      comments = response.comments
      console.log(comments)
      makeModal(e.target.parentNode, comments)
    },
  })

  $('#myModal').modal('show')
}
const makeModal = (e, comment) => {
  const title = e.children[1].innerText
  const cafeId = e.id
  const comments = [...comment]
  if ($('#modal-header')) {
    const modalContainer = document.getElementById('modal-header')
    modalContainer.innerHTML = `<h5 class="modal-title">${title}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>`

    const modalBody = document.getElementById('modal-body')
    modalBody.innerHTML = ''
    if (comments.length === 0) {
      modalBody.innerHTML = `<p>첫 후기를 남겨보세요:)</p>
            <form action=/post/seoul/${cafeId} method="post">
        <input type="text" name="content"/>
        <button type="submit" class="btn btn-primary">후기 등록</button>
      </form>
        `
    } else {
      for (i of comments) {
        modalBody.innerHTML += `
        <div class="content">
        <p>${i.content}</p>
        <p class="aa">${i.createdAt}</p>
        </div>`
      }
      modalBody.innerHTML += `
      <form action=/post/seoul/${cafeId} method="post">
        <input type="text" name="content"/>
        <button type="submit" class="btn btn-primary">후기 등록</button>
      </form>
        `
    }
  }
}

const aaa = document.getElementById('surprise')
aaa.addEventListener('click',surprise)
const surprise = ()=>{
  window.location.href='/surprise'
  } 
