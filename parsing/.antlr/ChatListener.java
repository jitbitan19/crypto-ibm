// Generated from /Users/jitbitan/Documents/Cryptography/parsing/Chat.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ChatParser}.
 */
public interface ChatListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ChatParser#chat}.
	 * @param ctx the parse tree
	 */
	void enterChat(ChatParser.ChatContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#chat}.
	 * @param ctx the parse tree
	 */
	void exitChat(ChatParser.ChatContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(ChatParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(ChatParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(ChatParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(ChatParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ChatParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ChatParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#mention}.
	 * @param ctx the parse tree
	 */
	void enterMention(ChatParser.MentionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#mention}.
	 * @param ctx the parse tree
	 */
	void exitMention(ChatParser.MentionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChatParser#msg}.
	 * @param ctx the parse tree
	 */
	void enterMsg(ChatParser.MsgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChatParser#msg}.
	 * @param ctx the parse tree
	 */
	void exitMsg(ChatParser.MsgContext ctx);
}