Vue.use(VueMaterial.default)

var vm = new Vue({
  el: '#app',
  data: {
    apiurl: '',

    id: '',

    date_from: '?',
    date_till: '?',
    
    new_date_from: null,
    new_date_till: null,
    
    items: Array,
    
    showDialog: false,
    message: ''
  },
  methods: {
    validate_id: function(id) {
        var vm = this
        pi = parseInt(id, 10)
        if (isNaN(pi) || String(pi) != id) {
          vm.dialog("Item id must be an integer!")
          return false
        }
        return true
    },
    validate_dates: function(date_from, date_till) {
      var vm = this
      if (date_from === null || date_till === null) 
      {
          vm.dialog("Both dates must be set!")
          return false
      }
      if (date_from > date_till) 
      {
          vm.dialog("The dates must be in order!")
          return false
      }
      return true
    },
    dialog: function (error) {
        var vm = this

        if (vm.apiurl == '')
            vm.message = 'please provide an API URL!'
        else if (typeof(error.data) !== 'undefined')
            vm.message = error.data.message
        else
            vm.message = String(error)
        
        vm.showDialog = true
    },
    fetch: function () {
      var vm = this
      
      idt = this.id.trim()
      if (vm.validate_id(idt) === false) return
      axios.get(vm.apiurl + '/item/' + idt)
        .then(function (response) {
          vm.date_from = response.data.date_from
          vm.date_till = response.data.date_till
        })
        .catch(function (error) {
          vm.date_from = "?"
          vm.date_till = "?"
          vm.dialog(error)
        })
    },
    add: function() {
      var vm = this
      if (vm.validate_dates(vm.new_date_from, vm.new_date_till) === false) return
      axios.post(vm.apiurl + '/items', {
          date_from: moment(vm.new_date_from).format("YYYY-MM-DD"),
          date_till: moment(vm.new_date_till).format("YYYY-MM-DD"),
          }).then(function () { 
              vm.dialog("OK!")
          })
          .catch(function (error) {
              vm.dialog(error)
          })
    },
    list: function() {
        var vm = this
        axios.get(vm.apiurl + '/items')
          .then(function (response) {
            if (response.data.length == 0)
              vm.dialog("No items to list!")
            vm.items = response.data
          }).catch(function (error) {
              vm.dialog(error)
          })
    }
  }
})
