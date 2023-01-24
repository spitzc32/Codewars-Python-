package kata

func ProductFib(prod uint64) [3]uint64 {
  a := uint64(0)
  b := uint64(1)
  bools := map[bool]uint64{false: 0, true: 1}
  
  for a * b < prod {
    a, b = b, a + b
  }
  
  return [3]uint64{a, b, bools[prod == a * b]}
}

func ProductFibSol1(prod uint64) [3]uint64 {
	var (
		a uint64 = 0
		b uint64 = 1
		i uint64 = 0
	)
	
	for i < prod {
	  i++
	  a,b = b,a+b
	  if a*b > prod { 
		return [3]uint64{a, b, 0} 
	  } else if a*b == prod {
		return [3]uint64{a, b, 1}
	  }
	}
	
	return [3]uint64{}
	  
  }