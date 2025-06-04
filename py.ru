def reverse_bits(n):
    # Convert to binary array.
    # The first digit is the beginning of the array.
    bits = n.digits(2)

    # Set length to 32 bits
    while bits.length < 32: do
        bits << 0
    end

    # Concatenate arrays and convert to binary numbers
    bits.join.to_i(2)
end
