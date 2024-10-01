export interface UserLoginResponse {
    success: boolean;
    access_token: string;
    token_type: string;
    user: string;
}