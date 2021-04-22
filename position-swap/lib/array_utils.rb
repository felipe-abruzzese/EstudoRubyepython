class ArrayUtils
  def troca(lista)
    n = 0
    lista_2 = []
    for n in (0..(lista.length-1))
      if n%2 == 0
      a = lista[n+1]
      lista_2 << a
    else
      b = lista[n-1]
      lista_2 << b
    end

  end
  print lista_2

  end
end
