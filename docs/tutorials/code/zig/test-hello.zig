const std = @import("std");

// Duck-typing the 'writer' parameter
pub fn hello(writer: anytype) !void {
    try writer.print("Hello, world!\n", .{});
}

// Sending output to STDOUT
pub fn main() !void {
    try hello(std.io.getStdOut().writer());
}

// Sending output to an array
test "hello writes 'Hello, world!' to stdout" {
    var output = std.ArrayList(u8).init(std.testing.allocator);
    defer output.deinit();
    try hello(output.writer());
    try std.testing.expectEqualStrings("Hello, world!\n", output.items);
}
