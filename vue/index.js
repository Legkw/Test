var watchExampleVM = new Vue({
  el: '#watch-example',
  data: {
    id: '',
    date_from: '?',
    date_till: '?',
    new_date_from: '',
    new_date_till: ''
  },
  methods: {
    get:  function () {
      var vm = this
      axios.get('http://localhost:5000/item/' + this.id)
        .then(function (response) {
          vm.date_from = response.data.date_from
          vm.date_till = response.data.date_till
        })
        .catch(function (error) {
          vm.date_from = "?"
          vm.date_till = "?"
        })
    },
    post:  function() {
      var vm = this
      axios.post('http://localhost:5000/items/', {
          date_from: vm.new_date_from,
          date_till: vm.new_date_till,
          })
    }
  }
})