const getUrlInfo = () => {
  //здесь адрес сервера
  const findParentA = (node) => {
    if (node.tagName == 'BODY') {
      return 0
    }
    else if (node.tagName == 'A') {
      return node
    } else {
      return findParentA(node.parentNode);
    }
  }  

  document.body.addEventListener('click', (event) => {
    event.preventDefault();
    let target = event.target;
    if(target.tagName != 'A') {
      target = findParentA(target);
    } 

    const checkPhishing = (checkingUrl) => {
      fetch(`http://45.84.1.197/phishing/?url=${checkingUrl}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Security-Policy': `script-src 'self' http://45.84.1.197/phishing/?url=${checkingUrl}`
        },
      }).then((res) => res.json()).then(json => {
        console.log(json);
        if(json.is_phishing) {
          alert('Данная ссылка находится в списке небезопасных, рекомендуем ее не посещать');
          location.reload();
        } else {
          location.href = target.href;
        }
        return json;
      }).catch(err => console.log(err));
    }

    if (target.tagName == 'A') {
      
      const urlInfo = checkPhishing(target.hostname); 
      console.log(urlInfo);
      return urlInfo
    }
    console.dir(target);
  });

  
}

const onResult = (ref) => {
  if (!ref[0]) {
    alert('URL access denied');
    return 0
  }

  const refName = document.createElement('p');
  refName.textContent = ref[0].result;
  modalContent.appendChild(refName);
}

const preprocessing = () => {
  chrome.tabs.query({
    active: true
  }, (tabs) => {
    const tab = tabs[0];
    if (tab) {
      chrome.scripting.executeScript({
        target: {
          tabId: tab.id,
          allFrames: false,
        },
        func: getUrlInfo,
      }, 
      onResult
      )
    } else {
      alert('No Active tabs');
    }
  })
}

document.addEventListener('DOMContentLoaded', preprocessing);
