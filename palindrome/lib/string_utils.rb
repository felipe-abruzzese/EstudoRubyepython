#class StringUtils
  def palindromo?(frase)
    frase = frase.delete(' ')
#    puts frase
    frase = frase.split('')
    frase = frase.map { |string| string.downcase  }
    frase << 0
    frase.rotate!(-1)
#    puts frase

    for i in (0..(frase.length-1))
      if frase[i] == frase[-i]
      else
        puts false
        break
      end
    end
  end
#end

palindromo?("Roma me tem amor")
