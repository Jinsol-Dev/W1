$(document).ready(function () {
  show_articles()
  console.log('hi')
})

function show_articles() {
  $.ajax({
    type: 'GET',
    url: '/board/get',
    data: {},
    success: function (response) {
      const boardArticles = [...response.articles]

      const accordion = document.getElementById('accordionExample')

      boardArticles.map((el) => {
        console.log(el.comments)
        const Item = document.createElement('div')
        Item.className = 'accordion-item'
        const targetId = '#collapse' + el._id
        const targetedId = 'collapse' + el._id

        if (el.comments.length === 0) {
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
              <article class="reply-article">
                <p>등록된 댓글이 없습니다.</p>
                <form action="/board/${el._id}" method="post" class="input-reply">
                  <input type="text" id="replyInput" name='content'/>
                  <input type="submit" value="등록" >
                </form>
              </article>
            </div>
          </div>
        </div>
     `
        } else {
          const firstDiv = document.createElement('div')
          firstDiv.className = 'accordion-item'
          const firsth2 = document.createElement('h2')
          firsth2.className = 'accordion-header'
          firsth2.setAttribute('id', 'headingTwo')
          const firstbtn = document.createElement('button')
          firstbtn.className = 'accordion-button'
          firstbtn.classList.add('collapsed')
          firstbtn.setAttribute('type', 'button')
          firstbtn.setAttribute('data-bs-toggle', 'collapse')
          firstbtn.setAttribute('data-bs-target', targetId)
          firstbtn.setAttribute('aria-expanded', 'false')
          firstbtn.setAttribute('aria-controls', 'collapseTwo')
          firstbtn.innerText = el.title
          firsth2.appendChild(firstbtn)

          const secondDiv = document.createElement('div')
          secondDiv.className = 'accordion-collapse'
          secondDiv.classList.add('collapse')
          secondDiv.setAttribute('id', targetedId)
          secondDiv.setAttribute('aria-labelledby', 'headingTwo')
          secondDiv.setAttribute('data-bs-parent', '#accordionExample')

          const thirdDiv = document.createElement('div')
          thirdDiv.className = 'accordion-body'
          const fourthDiv = document.createElement('div')
          fourthDiv.className = 'content-container'
          fourthDiv.innerText = el.content
          const firstArticle = document.createElement('article')
          firstArticle.className = 'reply-article'

          // const dateNow = new Date(el.comments.createdAt).toLocaleString()
          const commentsList = [...el.comments]
          commentsList.map((ele) => {
            console.log(ele)
            const replyContent = document.createElement('div')
            replyContent.className = 'reply-container'
            replyContent.innerHTML = `
            <p class="reply-content">${ele.content}</p>
            <p class="reply-created">${ele.createdAt}</p>
          `
            firstArticle.appendChild(replyContent)
          })
          const formDiv = document.createElement('form')
          formDiv.className = 'input-reply'
          formDiv.setAttribute('action', `/board/${el._id}`)
          formDiv.setAttribute('method', 'post')
          formDiv.innerHTML = `
          <input type="text" id="replyInput" name='content'/>
          <input type="submit" value="등록" ></input>
          `
          firstArticle.appendChild(formDiv)

          thirdDiv.appendChild(fourthDiv)
          thirdDiv.appendChild(firstArticle)
          secondDiv.appendChild(thirdDiv)
          firstDiv.appendChild(firsth2)
          firstDiv.appendChild(secondDiv)
          Item.appendChild(firstDiv)
        }
        accordion.appendChild(Item)
      })
    },
  })
}
