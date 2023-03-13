<template>
    <div>
        <Button text="Yes" color="green" action="console.log('cliecked')" path="/"/>
        <Button text="no" color="red" action="console.log('cliecked')" path="/"/>
    </div>
</template>

<script>
// import axios from 'axios';
import Button from '@/components/Button.vue'

export default {
    name:'del-Post',
    components:{
        Button
    },

    mounted(){
        console.log(this.$route)
    }
}
</script>

<style>

</style>