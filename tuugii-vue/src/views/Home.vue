<template>
  <div class="container">
    <Header title="Posts"/>
    <Button color="cyan" path="/Upload" text="Upload new Post"/>
    <tasks/>
    <component :is="currentView" />
  </div>
   
</template>

<script>
import Header from "../components/Header"
import tasks from "../components/tasks"
import Button from '../components/Button.vue'
export default {
  name: 'Home-page',
  components: {
    Header,
    tasks,
    Button
  },
  data(){
    return{
      tasks:[],
    }
  },
  created(){
    this.tasks = [
      {
        id: 1,
        text: "Doctor's appointment",
        day: 'march 1st at 2:30 pm',
        Desc: "have to get checked by the doctor for my hemmoroids",
        reminder: true
      },
      {
        id: 2,
        text: "shopping appointment",
        day: 'march 12st at 1:20 pm',
        Desc: "Going shopping with the worst person ever I hate my self",
        reminder: false
      },
      {
        id: 3,
        text: "pi day",
        day: 'march 14st at 9:00 am',
        Desc: "I have to count to 100th decimal of PI in a contest",
        reminder: false
      }
    ];
    
  }
}
</script>
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'Poppins', sans-serif;
}
.container {
  max-width: 900px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
