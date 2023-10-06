function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed.");
  }
  return a / b;
}

try {
  const result = divide(10, 0);
  console.log("Result:", result);
} catch (error) {
  console.error("Error:", error.message);
}
