$(document).ready(function () {
  show_articles()
})

function show_articles() {
  $.ajax({
    type: 'GET',
    url: '/board/get',
    data: {},
    success: function (response) {
      const boardArticles = [...response.articles]
      console.log(document.getElementById('userTrue').innerText)
      const userTrue = document.getElementById('userTrue').innerText

      const accordion = document.getElementById('accordionExample')
      const orderedDate = boardArticles.sort(
        (a, b) => new Date(b.createdAt) - new Date(a.createdAt),
      )
      orderedDate.map((el) => {
        const Item = document.createElement('div')
        Item.className = 'accordion-item'
        const targetId = '#collapse' + el._id
        const targetedId = 'collapse' + el._id
        const userName = el.createuser
        if (el.createuser) {
          if (userTrue === el.createuser) {
            console.log(el.title)

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
                <hr style="width:95%; height: 1px; background-color: black;">
              </div>
              <article class="reply-article">
                <p>등록된 댓글이 없습니다.</p>
                <form action="post/board/${el._id}" method="post" class="input-reply">
                  <input type="text" id="replyInput" name='content' placeholder="댓글을 입력해주세요."/>
                  <input type="submit" value="등록" style="margin-top: 0.5rem;">
                </form>
                <form action="del/board/${el._id}" method="post" class="input-reply" id= "delBtn" >
                  <input type="submit" value="게시글 삭제" style="margin-top: 0.5rem;" id='>
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

              const commentsList = [...el.comments]
              commentsList.map((ele) => {
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
              formDiv.setAttribute('action', `/post/board/${el._id}`)
              formDiv.setAttribute('method', 'post')
              formDiv.innerHTML = `
          <input type="text" id="replyInput" name='content' placeholder="댓글을 입력하세요."/>
          <input class="registration" type="submit" value="등록" style="margin-top: 0.5rem;"></input>
          `
              firstArticle.appendChild(formDiv)

              const formDiv1 = document.createElement('form')
              formDiv1.className = 'input-reply'
              formDiv1.setAttribute('action', `/del/board/${el._id}`)
              formDiv1.setAttribute('method', 'post')
              formDiv1.setAttribute('id', 'delBtn')
              formDiv1.innerHTML = `
          <input id= "delBtn" class="registration" type="submit" value="게시글 삭제" style="margin-top: 0.5rem;"></input>
          `
              firstArticle.appendChild(formDiv1)

              thirdDiv.appendChild(fourthDiv)
              thirdDiv.appendChild(firstArticle)
              secondDiv.appendChild(thirdDiv)
              firstDiv.appendChild(firsth2)
              firstDiv.appendChild(secondDiv)
              Item.appendChild(firstDiv)
            }
          }
        } else {
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
                <hr style="width:95%; height: 1px; background-color: black;">
              </div>
              <article class="reply-article">
                <p>등록된 댓글이 없습니다.</p>
                <form action="post/board/${el._id}" method="post" class="input-reply">
                  <input type="text" id="replyInput" name='content' placeholder="댓글을 입력해주세요."/>
                  <input type="submit" value="등록" style="margin-top: 0.5rem;">
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

            const commentsList = [...el.comments]
            commentsList.map((ele) => {
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
            formDiv.setAttribute('action', `/post/board/${el._id}`)
            formDiv.setAttribute('method', 'post')
            formDiv.innerHTML = `
          <input type="text" id="replyInput" name='content' placeholder="댓글을 입력하세요."/>
          <input class="registration" type="submit" value="등록" style="margin-top: 0.5rem;"></input>
          `
            firstArticle.appendChild(formDiv)

            thirdDiv.appendChild(fourthDiv)
            thirdDiv.appendChild(firstArticle)
            secondDiv.appendChild(thirdDiv)
            firstDiv.appendChild(firsth2)
            firstDiv.appendChild(secondDiv)
            Item.appendChild(firstDiv)
          }
        }
        accordion.appendChild(Item)
      })
    },
  })
}
