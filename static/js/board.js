$(document).ready(function () {
  show_articles()
  console.log('hi')
})

function show_articles() {
  console.log('hi')
  $.ajax({
    type: 'GET',
    url: '/board/get',
    data: {},
    success: function (response) {
      console.log('hi')
      const boardArticles = [...response.articles]
      console.log(boardArticles)

      const accordion = document.getElementById('accordionExample')

      boardArticles.map((el) => {
        const Item = document.createElement('div')
        Item.className = 'accordion-item'
        const targetId = '#collapse' + el._id
        const targetedId = 'collapse' + el._id
        const onlyId = 1
        Item.innerHTML = `
       <div class="accordion-item">
          <h2 class="accordion-header" id="headingTwo">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target=${targetId}
              aria-expanded="false" aria-controls="collapseTwo" > ${el.title}
          </h2>
          <div id=${targetedId}
            class="accordion-collapse collapse" aria-labelledby="headingTwo"
            data-bs-parent="#accordionExample" >
            <div class="accordion-body">
              <div class="content-container">
                ${el.content}
              </div>
              <article class="reply-article" id = ${onlyId}>
              </article>
            </div>
          </div>
        </div>
     `
        // const replybox = document.getElementById(onlyId)
        // console.dir(replybox)
        // if (!el.contents) {
        //   const p = document.createElement('p')
        //   p.innerText = '등록된 글이 없습니다.'
        //   replybox.appendChild(p)
        // }
        // accordion.appendChild(Item)
      })
    },
  })
}

//  <article class="reply-article">
//               <%if(!i.comments){%>
//                 <p>
//                   등록된 댓글이 없습니다.
//                 </p>
//               <%}else{%>
//                 <%for(i of i.comments){%>
//                   <div class="reply-container">
//                     <p class="reply-content"><%=i.content%></p>
//                     <p class="reply-created"><%=new Date(i.createdAt).toLocaleString()%></p>
//                   </div>
//                 <%}%>
//               <%}%>
//               <form action="/community/<%=i.id%>/comments" method="post" class="input-reply">
//                 <input type="text" id="replyInput" name='content'/>
//                 <input type="submit" value="등록" >
//               </form>
//             </article>
