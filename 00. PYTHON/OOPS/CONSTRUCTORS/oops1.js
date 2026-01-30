<script>
{
	class Person{
		constructor(name,age){
			this.name = name;
			this.age = age;
		}
		greet(){
			console.log(`Hi,My name is ${this.name}`)
		}
    }
  const p1 = new Person('Mahesh',27)
  const p2 = new Person('AB',27)
p1.greet();
p2.greet();
}
</script>