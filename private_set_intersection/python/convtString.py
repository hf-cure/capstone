def convert_and_save_rows(input_file, output_file):
    try:
        # Read rows and create string array with quotes
        with open(input_file, 'r') as infile:
            # Read lines, strip whitespace, add quotes
            string_array = [f"'{line.strip()}'" for line in infile if line.strip()]

        # Save to output file in array format
        with open(output_file, 'w') as outfile:
            outfile.write("[\n")
            for i, item in enumerate(string_array):
                outfile.write(f"    {item}")
                if i < len(string_array) - 1:
                    outfile.write(",")
                outfile.write("\n")
            outfile.write("]\n")

        print(f"Successfully processed {input_file} and saved to {output_file}")
        return string_array

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    input_filename = "hashed.txt"
    output_filename = "output.txt"
    convert_and_save_rows(input_filename, output_filename)