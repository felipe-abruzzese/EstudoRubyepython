#class Number
  def smallest_divisible(min, max)

      for i in (min..max)
        x = 4
        if x%i == 0
          if i == max
            puts "#{x} true"
          end
        else
          puts "false"
          false
          break
        end
      end
    end
  


smallest_divisible(1, 2)
