
class BoggleGame {

    constructor(board , seconds = 60 ){
        this.seconds = seconds;
        this.showTime();
        this.score = 0;
      
        


        this.timer = setInterval(this.ticker.bind(this) , 1000);
        this.board = $("." + board);
        $(".form").on("submit" , this.submitController.bind(this));
        
    }



    async submitController(evt){
        evt.preventDefault();
        // const res = await axios.get("/")
        const wordInput = $(".word")
        const word = $(".word").val()
        let $wordHolder = $(".word-holder" , this.board)
        let $message = $(".message-holder")
        const newWord = $(`<li>${word}</li>`)
        const res = await axios.get("/check-valid-word" , {params : {word: word}})
        const result = res.data.result
        console.log(result)
        if(word.length > 0 && result == "ok"){
            this.score += word.length
            $message.text("")
            $wordHolder.append(newWord)
            $message.append(result)
            wordInput.val("")
        }
        else if (word.length > 0 && result == "not-word" || result == "not-on-board"){
            $message.text("")
            $message.append(result)
        }
        
        
    }  




    showTime(){
        $(".timer" , this.board).text(this.seconds)
    }

    
    ticker(){
        this.seconds -= 1
        this.showTime()
        console.log(this.seconds)
        if(this.seconds === 0 ){
            clearInterval(this.timer)
            this.endGame()
        }

    }



    async endGame(){
        $(".word", this.board).hide();
        $(".btn", this.board).hide();
        let $message = $(".message-holder")
        $message.text("")
        $message.text(`score: ${this.score}`)
    }
 
    










}