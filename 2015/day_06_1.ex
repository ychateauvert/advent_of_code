#input = "turn on 0,0 through 999,999\ntoggle 0,0 through 999,0\nturn off 499,499 through 500,500" |> String.split("\n") |> Enum.map(&(String.split(&1, " ")))
input = "../inputs/day_06.txt" |> File.read! |> String.trim |> String.split("\n") |> Enum.map(&(String.split(&1, " ")))

turn = fn (matrix, [from_x, from_y], [to_x, to_y], val) ->
  for x <- from_x..to_x, y <- from_y..to_y, into: matrix, do: {{x, y}, val}
end

toggle = fn (matrix, [from_x, from_y], [to_x, to_y]) ->
  for x <- from_x..to_x, y <- from_y..to_y, into: matrix, do: { {x, y}, !Map.get(matrix, {x, y}) }
end

coord = fn (coord) ->
  [x, y] = String.split(coord, ",")
  [String.to_integer(x), String.to_integer(y)]
end

matrix = for x <- 0..999, y <- 0..999, into: %{}, do: {{x, y}, false}
matrix = Enum.reduce input, matrix, fn 
  (["turn", "on", start_pos, _, end_pos], acc) -> turn.(acc, coord.(start_pos), coord.(end_pos), true)
  (["turn", "off", start_pos, _, end_pos], acc) -> turn.(acc, coord.(start_pos), coord.(end_pos), false)
  (["toggle", start_pos, _, end_pos], acc) -> toggle.(acc, coord.(start_pos), coord.(end_pos))
end

matrix
|> Map.values
|> Enum.filter(&(&1 === true))
|> length
|> IO.puts
