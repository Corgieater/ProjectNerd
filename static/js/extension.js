"use strict";
const tagInput = document.querySelector("#tagInput");
const tagWrap = document.querySelector("#tagWrap");
const tagList = document.querySelector("#tagList");
const tagSuggestions = document.querySelector(".tagSuggestions");
let enterCount = 0;
let timer;
// 刪除tags用
let isLastChar = false;
let backspaceCounts = 0;

// 要做的事: 點suggestions可以直接做tag貼上
// 得到該user的所有list [{'name': list ID}]
// add new list

// 處理刪除tag的問題
// 偵測到input沒東西且前面有其他tag就要砍tag
tagInput.addEventListener("keydown", (e) => {
  const tag = tagInput.value;
  let previousTag = tagWrap.previousElementSibling;
  if (e.key === "Backspace" && tag === "" && previousTag) {
    tagWrap.parentNode.removeChild(previousTag);
  }
});

tagInput.addEventListener("keyup", async (e) => {
  const tag = tagInput.value;
  if (!tag) return;
  if (e.key !== "Enter") {
    clearTimeout(timer);
    timer = setTimeout(async function () {
      if (tag.length >= 2) {
        let hotTags = await getTagList(`http://127.0.0.1:8000/tag/${tag}`);
        let hotTagsLength = hotTags.length;
        if (hotTags !== false) {
          tagSuggestions.classList.remove("hide");
          makeAtagsToTagSuggestions(hotTags, hotTagsLength);
        } else {
          console.log("no words");
          // **********remember it and call api create tag**********
        }
      }
    }, 1000);
  }

  //   送出就加tag到畫面 到時候也要處理資料的部分
  //   tag suggestions打API要資料 現在在想辦法阻擋別人一直猛key癱瘓API
  if (e.key === "Enter") {
    const tagElement = document.createElement("span");
    tagElement.textContent = `# ${tag}`;
    tagList.insertBefore(tagElement, tagWrap);
    tagSuggestions.classList.add("hide");
    tagInput.value = "";
  }

  if (e.key === "Backspace" && tag.length === 1) {
    tagSuggestions.classList.add("hide");
  }
});

// 關鍵字拿資料庫tags
async function getTagList(url) {
  try {
    const res = await fetch(url);
    const req = await res.json();
    console.log(req);
    if (!req.ok) {
      return false;
    } else {
      console.log(req.tags);
      return req.tags;
    }
  } catch (err) {
    console.log(`error:${err}`);
  }
}

// 做a tags
function makeAtagsToTagSuggestions(hotTagObj, amount) {
  removeAtagsInTagSuggestions();
  for (let i = 0; i < amount; i++) {
    const a = document.createElement("a");
    const tagName = Object.keys(hotTagObj[i]);
    const tagId = Object.values(hotTagObj[i]);
    a.textContent = tagName;
    a.rel = tagId;
    a.href = "#";
    // 點下tag suggestion後．tag視覺化
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const tagElement = document.createElement("span");
      tagElement.textContent = `# ${tagName}`;
      tagList.insertBefore(tagElement, tagWrap);
      tagSuggestions.classList.add("hide");
      tagInput.value = "";
      console.log(a.rel, a.textContent);
      return [a.rel, a.textContent];
    });
    a.classList.add("list-group-item");
    a.classList.add("list-group-item-action");
    tagSuggestions.appendChild(a);
  }
}

// remove old tags from tagSuggestions
function removeAtagsInTagSuggestions() {
  tagSuggestions.innerHTML = `<div
  class="list-group-item list-group-item-action active" aria-current="true">
    熱門標籤
  </div>`;
}

// show or hide tag suggestions
function showOrHide(el) {
  console.log("showOrHide active");
  if (el.classList.contains("hide")) {
    el.classList.remove("hide");
    console.log("remove hide");
  } else {
    el.classList.add("hide");
    console.log("add hide");
  }
}

// detect if need delete some tagSuggestions or add some
// function makeSuggestions(oldATagsLength, hotTagsLength, hotTagObj) {
//   showOrHide(tagSuggestions);
//   if (oldATagsLength === 0) {
//     for (let i = 0; i < hotTags.length; i++) {
//       let tagName = Object.keys(hotTagObj[i]);
//       let tagId = Object.values(hotTagObj[i]);
//       makeAtags(tagName, tagId);
//     }
//     // 如果已有舊搜尋結果表示list已經做出來了
//     // 舊搜尋結果如果跟新搜尋結果長度一樣，就不用做了，直接替換
//     // 重複的部分怎處理? 包裝成一個功能
//   } else if (oldATagsLength === hotTagsLength) {
//     for (let i = 0; i < oldATagsLength; i++) {
//       oldATags[i].textContent = Object.keys(hotTags[i]);
//       oldATags.erl = Object.values(hotTags[i]);
//     }
//   } else if (oldATagsLength !== hotTagsLength) {
//     let gapRange = 0;
//     if (oldATagsLength > hotTagsLength) {
//       gapRange = oldATagsLength - hotTagsLength;
//       for (let i = 0; i < gapRange; i++) {
//         tagSuggestions.removeChild(oldATags[i]);
//       }
//     } else {
//       gapRange = hotTagsLength - oldATagsLength;
//       for (let i = 0; i < gapRange; i++) {
//         let tagName = Object.keys(hotTags[i]);
//         let tagId = Object.values(hotTags[i]);
//         makeAtags(tagName, tagId);
//       }
//     }
//   }
// }
