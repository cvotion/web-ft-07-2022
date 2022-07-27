
        function newDiv(attribute){
            let div = document.createElement('div')
            div.setAttribute('class', attribute)
            return div
        }
        let header = document.createElement('header')
        let br1 = document.createElement('br')
        let br2 = document.createElement('br')
        let br3 = document.createElement('br')
        let main = document.createElement('main')
        let body = document.querySelector('body')

    // Header
        let div1 = newDiv('row')
        let div2 = newDiv('col display-2 text-white')
        div2.innerText = "HighOnCoding"
        let div3 = newDiv('col')
        let div4 = newDiv('row')
        let div5 = newDiv('col-3 display-6 text-white')
        div5.innerText = "Home"
        let div6 = newDiv('col display-6 text-white')
        div6.innerText = "Categories"
    
        div4.append(div5)
        div4.append(div6)
        div3.append(div4)
        div1.append(div2)
        div1.append(div3)
        header.append(div1)
        header.append(br1)

    // Main
        main.setAttribute('class', 'p-5')
        let mainDiv1 = newDiv('lightgray p-2')
        // div 1    
        let div1child1 = newDiv('title display-6 gray')
        div1child1.innerText = "Curse of the Current Reviews"
        mainDiv1.append(div1child1)
        let div1child2 = newDiv('lead')
        div1child2.innerText = 'When you want to buy an application from the Apple iTunes store you have miore choices than you can handle. Most of the users scroll past the apploication description completly avoiding it like ads displaued on the right column of your webpage. Their choice is dependent on three important factors; price, screenshot, and reviews.'
        mainDiv1.append(div1child2)
        mainDiv1.append(br2)
        main.append(mainDiv1)
        
        // div 2
        
        let mainDiv2 = newDiv('section2')
        let d1 = newDiv("text-primary display-6")
        d1.innerText = "Hello WatchKit"
        mainDiv2.append(d1)
        let d2 = newDiv('lead')
        d2.innerText = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nihil, incidunt. Commodi cum exercitationem voluptatum maiores quam aliquid, cumque alias, unde veniam aspernatur sunt necessitatibus accusantium animi! Natus perferendis reprehenderit voluptatibus."
        mainDiv2.append(d2)
        let d3 = newDiv('row orange text-white')
        let d3a = newDiv("col-2")
        d3a.innerText = "12 comments"
        d3.append(d3a)
        let d3b = newDiv("col-2")
        d3b.innerText = "124 likes"
        d3.append(d3b)
        mainDiv2.append(d3)
        mainDiv2.append(br3)
        main.append(mainDiv2)
        
        
        // div 3
        
        let mainDiv3 = newDiv('section3')
        let a = newDiv("text-primary display-6")
        a.innerText = "Hello WatchKit"
        mainDiv3.append(a)
        let b = newDiv('lead')
        b.innerText = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nihil, incidunt. Commodi cum exercitationem voluptatum maiores quam aliquid, cumque alias, unde veniam aspernatur sunt necessitatibus accusantium animi! Natus perferendis reprehenderit voluptatibus."
        mainDiv3.append(b)
        let c = newDiv('row orange text-white')
        let c1 = newDiv("col-2")
        c1.innerText = "12 comments"
        c.append(c1)
        let c2 = newDiv("col-2")
        c2.innerText = "124 likes"
        c.append(c2)
        mainDiv3.append(c)
        mainDiv3.append(br3)
        main.append(mainDiv3)

        body.append(header)
        body.append(main)
    
        
        
        // body.append(header)